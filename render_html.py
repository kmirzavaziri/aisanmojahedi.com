import yaml

import jinja2


def main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."))

    with open("cv/Aisan_Mojahedi_CV.yaml", "r") as f:
        web_yaml = render_j2_by_yaml(env, "web.yaml", f)

    with open("public/index.html", "w") as f:
        f.write(render_j2_by_yaml(env, "templates/index.html.j2", web_yaml))


def render_j2_by_yaml(env, template_filename, yaml_stream):
    return env.get_template(template_filename).render(yaml.safe_load(yaml_stream))


if __name__ == "__main__":
    main()
