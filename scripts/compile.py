import glob, sys
import yaml
import frontmatter

files = glob.glob('{}/*.def'.format(sys.argv[1]))

glossary_entry = """
\\newglossaryentry{{{}}}{{
   name = {{{}}},
   description = {{{}}},
symbol = {{\ensuremath {}}}
}}
"""

glossary = ""


for filename in files:
    content = frontmatter.load(filename)

    if "label" not in content.keys():
        label = content['title']
    else:
        label = content['label']

    if "symbol" in content.keys():
        symbol = content['symbol']
    else:
        symbol = ""
        
    glossary += glossary_entry.format(label.lower(),
                                content['title'],
                                      content.content,
                                      symbol)
    

with open("glossary.tex", "w") as output :
    output.write(glossary)

