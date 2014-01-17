import os.path
import string
import glob

print " "
print "Generate assertj HTML files"

# load content
with open('site/assertj-top-menu.html') as menu_file:
    menu_content = menu_file.read()
with open('site/assertj-head.html') as head_file:
    head_content = head_file.read()
with open('site/assertj-footer.html') as footer_file:
    footer_content = footer_file.read()
with open('site/assertj-javascript.html') as javascript_file:
    javascript_content = javascript_file.read()
with open('site/assertj-core-side-menu.html') as assertj_core_side_menu_file:
    assertj_core_side_menu_content = assertj_core_side_menu_file.read()
with open('site/assertj-news-side-menu.html') as assertj_news_side_menu_file:
    assertj_news_side_menu_content = assertj_news_side_menu_file.read()
with open('site/assertj-guava-side-menu.html') as assertj_guava_side_menu_file:
    assertj_guava_side_menu_content = assertj_guava_side_menu_file.read()
with open('site/assertj-neo4j-side-menu.html') as assertj_neo4j_side_menu_file:
    assertj_neo4j_side_menu_content = assertj_neo4j_side_menu_file.read()
with open('site/assertj-joda-time-side-menu.html') as assertj_jodatime_side_menu_file:
    assertj_jodatime_side_menu_content = assertj_jodatime_side_menu_file.read()
with open('site/assertj-assertions-generator-side-menu.html') as assertj_assertions_generator_side_menu_file:
    assertj_assertions_generator_side_menu_content = assertj_assertions_generator_side_menu_file.read()
# stores it into a map for later substitution
template_data_map = {'menu': menu_content,
                     'head': head_content,
                     'footer': footer_content,
                     'javascript': javascript_content,
                     'assertj_core_side_menu': assertj_core_side_menu_content,
                     'assertj_news_side_menu': assertj_news_side_menu_content,
                     'assertj_guava_side_menu': assertj_guava_side_menu_content,
                     'assertj_neo4j_side_menu': assertj_neo4j_side_menu_content,
                     'assertj_jodatime_side_menu': assertj_jodatime_side_menu_content,
                     'assertj_assertions_generator_side_menu': assertj_assertions_generator_side_menu_content}

initial_dir = os.getcwd()
templates_dir = "templates"
os.chdir(templates_dir)

for template_file_name in glob.glob("*-template.html"):
    target_file_name = '../site/' + template_file_name.replace('-template.html', '.html')
    print "-- generate " + target_file_name + " from " + template_file_name
    # open the file and read content
    template_file_path = os.path.join(os.path.dirname(__file__), template_file_name)
    with open(template_file_path) as index_template_file:
        target_file_name_content = string.Template(index_template_file.read())

    # resolve template variables
    target_file_name_content = target_file_name_content.safe_substitute(template_data_map)

    with open(target_file_name, "w") as target_file:
        target_file.write(target_file_name_content)

os.chdir(initial_dir)
