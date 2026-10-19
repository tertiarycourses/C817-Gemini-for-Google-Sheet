"""
Parse a lab's steps (data_domainN.py) into its ordered Gemini prompts. Shared by
build_prompts_page.py (the web page), build_labs.py (the PDF, sample-prompts.txt
and the pre-filled Prompt_Log sheet in each lab workbook), so all of them always
list the same prompts in the same order.

A step's code block holds prompts, formulas or reference info. A label at the
start of a paragraph says which, and where the learner sends it:

  ASK GEMINI:   a question in the Gemini side panel - the answer stays in the panel
  INSERT:       Gemini generates a table, text or chart - you choose Insert
  ACTION:       Gemini shows an action preview card - you choose Apply (or Undo)
  FORMULA:      a formula request in the side panel - you choose Insert into a cell
  GEM:          a prompt to your Gem (Gems in the side panel, or the Gemini app)
  GEMINI APP:   a prompt in the Gemini app at gemini.google.com
  FOLLOW-UP:    refines the previous answer before you insert it
  CHECK (...):  a check Gemini performs; CHECK: followed by =formulas is typed by you
  AI FUNCTION:  =AI(...) formulas you type into cells, then Generate and insert
  LOG:          fills in the Prompt_Log sheet
"""
import re

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

LABEL = re.compile(r"^(ASK GEMINI|INSERT|ACTION|FORMULA|GEMINI APP|GEM|FOLLOW-UP|CHECK FORMULAS|CHECK|LOG|"
                   r"AI FUNCTION|OPTION [A-Z]|Then|Expected)([^:\n]*):[ \t]*(.*)$")
TAGS = {
    "ASK GEMINI": "Ask Gemini · answer in the panel",
    "INSERT": "Ask Gemini · then Insert",
    "ACTION": "Ask Gemini · then Apply",
    "FORMULA": "Formula · then Insert",
    "GEM": "Your Gem",
    "GEMINI APP": "Gemini app · gemini.google.com",
    "FOLLOW-UP": "Follow-up",
    "LOG": "Log",
}
# Prompt_Log "Where" column
WHERE = {
    "Ask Gemini · answer in the panel": "Ask",
    "Ask Gemini · then Insert": "Insert",
    "Ask Gemini · then Apply": "Action",
    "Formula · then Insert": "Formula",
    "Your Gem": "Gem",
    "Gemini app · gemini.google.com": "Gemini app",
    "Follow-up": "Follow-up",
    "Log": "Ask",
}
INFO_LINE = re.compile(r"^[A-Za-z_][A-Za-z_ ()]*\s+:\s")      # "Sheets    : About_This_Data | ..."
FORMULA_LINE = re.compile(r"^(.*?\S)\s+(=\S.*)$")             # "Total rows   =COUNTA(A2:A244)"

STRUCT = re.compile(r"^(\(?\d+\)\s|[A-Z][A-Za-z0-9_]*( [A-Za-z0-9_]+)?:|- |=|[A-Z]\d+ )|\s=[A-Z<(]")


def unwrap(body):
    """Undo the source's ~100-column hard wraps; keep structural breaks (labels, numbered/indented items)."""
    out = []
    for line in body.split("\n"):
        s, indent = line.lstrip(), len(line) - len(line.lstrip())
        prev = out[-1].rstrip() if out else ""
        structural = (not out or not s or not prev or prev.isupper() or prev.endswith(":") or STRUCT.search(s)
                      or (1 <= indent <= 4 and s[0].isupper())
                      or s.startswith("##") or prev.startswith("##")
                      or (prev.endswith((".", "?")) and s[0].isupper()))
        if structural:
            out.append(line.rstrip())
        else:
            out[-1] = out[-1].rstrip() + " " + s.rstrip()
    return "\n".join(out)


def reflow(cmd):
    """A step's code block for print: prompt paragraphs are unwrapped so they wrap naturally;
    reference blocks ("Sheets : ...") and formula lines keep their line breaks."""
    out = []
    for para in re.split(r"\n\s*\n", cmd.strip("\n")):
        lines = para.split("\n")
        out.append(para if any(INFO_LINE.match(l.strip()) for l in lines) else unwrap(para))
    return "\n\n".join(out)


def split_formulas(body):
    """One item per line starting with '='; continuation lines are joined. A 'Label  =formula' line keeps its label."""
    out = []
    for line in body.split("\n"):
        s = line.strip()
        if not s:
            continue
        m = FORMULA_LINE.match(s)
        if m and not s.startswith("="):
            out.append([m.group(1), m.group(2)])
        elif s.startswith("=") or not out:
            out.append(["", s])
        else:
            out[-1][1] += " " + s
    return [tuple(x) for x in out]


def split_changes(body):
    """'One change at a time' blocks: one prompt per numbered item."""
    parts = re.split(r"^\d\)\s+", body, flags=re.M)
    return [re.sub(r"\s*\n\s*", " ", p).strip() for p in parts if p.strip()]


def parse_step(num, instr, cmd, mode=None):
    """Return (items, None). Items: ('prompt', tag, text) | ('formulas', tag, [(label, f)]) | ('info', tag, text)."""
    items = []
    if not cmd.strip():
        return items, None
    for para in re.split(r"\n\s*\n", cmd.strip("\n")):
        lines = para.rstrip().split("\n")
        m = LABEL.match(lines[0].strip())
        label = (m.group(1) + m.group(2)).strip() if m else None
        body = "\n".join(([m.group(3)] if m and m.group(3) else []) + lines[1:]) if m else para
        body = "\n".join(l.rstrip() for l in body.split("\n")).strip("\n")
        if label is None:
            if items and items[-1][0] == "prompt" and not INFO_LINE.match(lines[0]):
                # a multi-paragraph prompt (e.g. Gem instructions): later paragraphs belong to it
                kind, tag, text = items[-1]
                items[-1] = (kind, tag, text + "\n\n" + body)
                continue
            if num == 1 or INFO_LINE.match(lines[0]):
                items.append(("info", "Reference", body))
            elif all(FORMULA_LINE.match(l.strip()) or l.strip().startswith("=") for l in lines if l.strip()):
                items.append(("formulas", "Type these yourself", split_formulas(body)))
            else:
                items.append(("prompt", TAGS["ASK GEMINI"], body))
            continue
        base = label.split(" (")[0]
        sub = re.search(r"\(([^)]*)\)", label)
        if base in ("ASK GEMINI", "INSERT", "ACTION", "FORMULA", "GEM", "GEMINI APP", "FOLLOW-UP", "LOG"):
            tag = TAGS[base]
            if re.match(r"^1\)\s", body):            # numbered list: one prompt per change
                for chunk in split_changes(body):
                    items.append(("prompt", tag, chunk))
            else:
                items.append(("prompt", tag, body))
        elif base == "AI FUNCTION":
            items.append(("formulas", "AI function · type in the cell, then Generate and insert", split_formulas(body)))
        elif base.startswith("CHECK"):
            if body.lstrip().startswith("=") or all(FORMULA_LINE.match(l.strip()) for l in body.split("\n") if l.strip()):
                items.append(("formulas", "Check" + (" · " + sub.group(1) if sub else ""), split_formulas(body)))
            else:
                items.append(("prompt", "Check · " + (sub.group(1) if sub else "Ask Gemini"), body))
        elif base.startswith("OPTION"):
            items.append(("prompt", "Option" + base[6:], body))
        elif base == "Then":
            items.append(("prompt", TAGS["FOLLOW-UP"], body))
        else:  # Expected
            items.append(("info", label, body))
    return items, None


def _where(tag):
    if tag in WHERE:
        return WHERE[tag]
    if tag.startswith("Check · "):
        return {"Ask Gemini": "Ask"}.get(tag[8:], tag[8:])
    return "Ask"


def prompt_rows(lab):
    """Every Gemini prompt in step order: dicts with step, letter, tag, where (Prompt_Log) and the unwrapped text."""
    rows = []
    for i, (instr, cmd) in enumerate(lab["steps"], 1):
        items, _ = parse_step(i, instr, cmd)
        for kind, tag, body in items:
            if kind != "prompt":
                continue
            rows.append(dict(step=i, letter=LETTERS[len(rows)], tag=tag, mode=_where(tag), text=unwrap(body)))
    return rows
