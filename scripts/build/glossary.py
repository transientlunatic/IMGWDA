from PyOrgMode import PyOrgMode
import sys



def parse_org_file(filename):
    """
    Parse the contents of an org-mode format glossary file which
    stores a glossary using column-view.

    Parameters
    ----------
    filename : str
       The name of the file which contains the glossary.

    """
    base = PyOrgMode.OrgDataStructure()
    base.load_from_file(filename)
    entries = []
    for line in base.root.content:
        entry = {}
        if hasattr(line, "heading"):
            entry['name'] = line.heading
            entry['description'] = ""
            for descline in line.content:
                if hasattr(descline, "content"):
                    for orgproperty in descline.content:
                        if descline.TYPE == "DRAWER_ELEMENT":
                            try:
                                entry[orgproperty.name] = orgproperty.value
                                #print("+ {} : {}".format(orgproperty.name, orgproperty.value))
                            except AttributeError:
                                #print(orgproperty)
                                pass
                else:
                    entry['description'] += descline.replace("\n", " ")
        entries.append(entry)
    return entries

def export_latex(entries):
    """
    Produce a LaTeX-formatted glossary, using `glossaries`.
    """

    for entry in entries:
        if "ABBREVIATION" in entry:
            print("\\newacronym{{{}}}{{{}}}{{{}}}".format(entry['ABBREVIATION'].lower(), entry['ABBREVIATION'], entry['name']))

    for entry in entries:
        if ("name" in entry) and ("description" in entry):
            print("\\newglossaryentry{{{}}} {{ name={{{}}}, description={{{}}} }}".format(entry['name'].lower().replace(" ", "-"), entry['name'], entry['description']))


def main():
    filename = sys.argv[1]
    entries = parse_org_file(filename)
    export_latex(entries)

if __name__ == "__main__":
    main()
