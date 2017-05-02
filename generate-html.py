import os.path
import string
import glob


def content_of(filename):
    with open("./template-data/" + filename) as file_to_read:
        return file_to_read.read()

print (" ")
print ("Generate assertj HTML files")

# stores it into a map for later substitution
template_data_map = {
    'menu': content_of('assertj-top-menu.html'),
    'head': content_of('assertj-head.html'),
    'footer': content_of('assertj-footer.html'),
    'javascript': content_of('assertj-javascript.html'),
    'assertj_core_side_menu': content_of('assertj-core-side-menu.html'),
    'assertj_swing_danger_two_robots': content_of('assertj-swing-danger-two-robots.html'),
    'assertj_swing_get_it': content_of('assertj-swing-get-it.html'),
    'assertj_swing_name': "AssertJ Swing",
    'assertj_swing_sample_with_base_test': content_of('assertj-swing-sample-with-base-test.html'),
    'assertj_swing_sample_without_base_test': content_of('assertj-swing-sample-without-base-test.html'),
    'assertj_swing_side_menu': content_of('assertj-swing-side-menu.html'),
    'assertj_news_side_menu': content_of('assertj-news-side-menu.html'),
    'assertj_guava_side_menu': content_of('assertj-guava-side-menu.html'),
    'assertj_neo4j_side_menu': content_of('assertj-neo4j-side-menu.html'),
    'assertj_db_side_menu': content_of('assertj-db-side-menu.html'),
    'assertj_jodatime_side_menu': content_of('assertj-joda-time-side-menu.html'),
    'assertj_assertions_generator_side_menu': content_of('assertj-assertions-generator-side-menu.html')
}

initial_dir = os.getcwd()
templates_dir = "templates"
os.chdir(templates_dir)

for template_file_name in glob.glob("*-template.html"):
    target_file_name = '../' + template_file_name.replace('-template.html', '.html')
    print ("-- generate " + target_file_name + " from " + template_file_name)
    # open the file and read content
    template_file_path = os.path.join(os.path.dirname(__file__), template_file_name)
    with open(template_file_path) as index_template_file:
        target_file_name_content = string.Template(index_template_file.read())

    # resolve template variables
    target_file_name_content = target_file_name_content.safe_substitute(template_data_map)

    with open(target_file_name, "w") as target_file:
        target_file.write(target_file_name_content)

os.chdir(initial_dir)
