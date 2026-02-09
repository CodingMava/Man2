from django.template import Origin, TemplateDoesNotExist
from django.template.loaders.base import Loader as BaseLoader

TEMPLATES_DATA = {
    # ⬇️ paste THE ENTIRE TEMPLATES_DATA dict here
}

class DictTemplateLoader(BaseLoader):
    is_usable = True

    def get_template_sources(self, template_name):
        if template_name in TEMPLATES_DATA:
            yield Origin(
                name=template_name,
                template_name=template_name,
                loader=self,
            )

    def get_contents(self, origin):
        try:
            return TEMPLATES_DATA[origin.template_name]
        except KeyError:
            raise TemplateDoesNotExist(origin.template_name)
