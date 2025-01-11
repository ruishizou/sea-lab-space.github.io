#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import bibtexparser

# import bib file (from Zotero)
# can be updated to other files in future
bib_file = "./sea-lab-publication.bib"

# Function to convert name from 'Last, First' to 'First Last'
def convert_name(name):
    if ',' in name:
        last, first = [part.strip() for part in name.split(',', 1)]
        return f"{first} {last}"
    else:
        return name.strip()

# Function to convert name from 'First Last' to 'Last, First'
def reverse_name(name):
    parts = name.strip().split()
    if len(parts) >= 2:
        first = ' '.join(parts[:-1])
        last = parts[-1]
        return f"{last}, {first}"
    else:
        return name.strip()


# The latest version of the collaboration maintainance xlsx

collab_rename_csv = "./processing/Lab Collaboration Track Record - Person-Pub.csv"

df_author = pd.read_csv(collab_rename_csv)

# Build a mapping from any name (full_name or alias) to full_name
name_to_fullname = {}

for index, row in df_author.iterrows():
    full_name = row['Full Name']
    aliases = row['Alias']
    # Add the full name to the mapping
    name_to_fullname[full_name] = full_name
    if pd.notna(aliases):
        # Split aliases by ';' and strip whitespace
        alias_list = [alias.strip() for alias in aliases.split(';')]
        for alias in alias_list:
            name_to_fullname[alias] = full_name

# Read the bib file
with open(bib_file, 'r', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Keep track of names not found in df_author
names_not_found = set()

# Process each bib entry
for entry in bib_database.entries:
    if 'author' in entry:
        authors_str = entry['author']
        # Split authors by ' and '
        authors_list = [author.strip() for author in authors_str.split(' and ')]
        updated_authors = []
        for author in authors_list:
            # Convert author name to 'First Last' format
            author_name = convert_name(author)
            # Try to find the author in the mapping
            if author_name in name_to_fullname:
                full_name = name_to_fullname[author_name]
                # Convert full_name back to 'Last, First' format
                updated_author = reverse_name(full_name)
                updated_authors.append(updated_author)
            else:
                # Author not found, keep original name and add to names_not_found
                updated_authors.append(author)
                names_not_found.add(author_name)
        # Update the author field with updated author names
        entry['author'] = ' and '.join(updated_authors)

# Print out the names not found in df_author
print("Names not found in df_author:")
for name in names_not_found:
    print(name)

bib_process_file = "./sea-lab-publication.bib"
# Write the updated bib file
with open(bib_process_file, 'w', encoding='utf-8') as bibtex_file:
    bibtexparser.dump(bib_database, bibtex_file)


