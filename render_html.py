import sys

import yaml

import jinja2


def main():
    if len(sys.argv) != 5:
        raise Exception('pass exactly these parameters: cv_data web_data template output')

    cv_data, web_data, template, output = sys.argv[1:]

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."))

    with open(cv_data, 'r') as f:
        web_yaml = render_j2_by_yaml(env, web_data, f)

    with open(output, 'w') as f:
        f.write(render_j2_by_yaml(env, template, web_yaml))


def render_j2_by_yaml(env, template_filename, yaml_stream):
    return env.get_template(template_filename).render(yaml.safe_load(yaml_stream))


if __name__ == "__main__":
    main()
