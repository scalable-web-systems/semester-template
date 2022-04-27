import re
import requests
# Get all markdown files in the directory 
def get_file_names():
    import os

    exceptions = ['README.md']
    files = os.listdir('.')
    file_names = []

    for file in files:
        if '.md' in file and file not in exceptions:
            print(file)
            file_names.append(file)
    return file_names


# Check the PR has only Markdown files
# def test_check_only_md():
#     import os

#     files = os.listdir('.')

#     exceptions = ['README.md', 'test_md.py']
    
#     for file in files:
#         if '.md' not in file or file not in exceptions:
#             assert False
    
#     assert True


# Check for comment in the first line
def test_check_comment():
    for file_name in get_file_names():
        with open(file_name, 'r') as f:
            text = f.read()
            first_line = text.split('\n')[0]
            if('<!--' in first_line and '-->' in first_line):
                assert True
            else: 
                assert False

# Check basic content in the markdown files
def test_check_md_content():
    for file_name in get_file_names():
        with open(file_name, 'r') as f:
            text = f.read()

            if "Author" not in text:
                assert False

            if "Acknowledgements" not in text:
                assert False

            if "Feedback" not in text:
                assert False
            
        
        assert True

# Check all links are working in the markdown file
def test_check_urls():
    for file_name in get_file_names():
        with open(file_name, 'r') as f:
            text = f.read()
            urls = re.findall("(?P<url>https?://[^\s]+)", text)
            for url in urls:
                url = url.replace(')', '')
                try:
                    r = requests.get(url)
                    if r.status_code == 200 or r.status_code >= 500 or r.status_code == 403:
                        continue
                    else:
                        assert False
                except requests.exceptions.RequestException as err:
                    print ("OOps: Something Else",err)
                except requests.exceptions.HTTPError as errh:
                    print ("Http Error:",errh)
                except requests.exceptions.ConnectionError as errc:
                    print ("Error Connecting:",errc)
                except requests.exceptions.Timeout as errt:
                    print ("Timeout Error:",errt)   
            
    
    assert True





