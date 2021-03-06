from secrender import secrender, get_template_args
import datetime
import os
from yaml import full_load


class TestTemplateArgs:
    def test_simple(self):
        yaml = dict(x="1", y="fred")
        root = None
        set_ = None
        template_args = get_template_args(yaml, root, set_)
        assert set(template_args.keys()) == {"current_date", "x", "y"}
        assert template_args["x"] == "1"
        assert template_args["y"] == "fred"
        assert isinstance(template_args["current_date"], datetime.datetime)

    def test_with_set(self):
        yaml = dict(x="1", y="fred")
        root = None
        set_ = dict(y="2")
        template_args = get_template_args(yaml, root, set_)
        assert set(template_args.keys()) == {"current_date", "x", "y"}
        assert template_args["x"] == "1"
        assert template_args["y"] == "2"
        assert isinstance(template_args["current_date"], datetime.datetime)

    def test_secrender_examples(self, tmp_path):
        yaml = full_load(open("examples/example.yaml"))
        root = None
        set_ = None
        template_path = "examples/example.md.j2"
        template_args = get_template_args(yaml, root, set_)
        output_path = tmp_path / "example.md"
        secrender(template_path, template_args, output_path)
        assert os.path.isfile(output_path)
        contents = open(output_path, "r").read()
        assert len(contents) > 0
        assert "Today is" in contents
        assert "My pets" in contents
        assert "Rover has black fur" in contents
        assert "Felix has brown fur" in contents
