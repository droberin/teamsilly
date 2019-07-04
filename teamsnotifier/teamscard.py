class TeamsCard:
    _card_name = None
    _default_activity_image = 'https://teamsnodesample.azurewebsites.net/static/img/image5.png'
    _default_activity_title_image = 'https://47a92947.ngrok.io/Content/Images/default.png'
    structure = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "summary": "Task or action summary not defined...",
        "sections": [{
            "activityTitle": f"![TestImage]({_default_activity_title_image})Task or action summary not defined...",
            "activitySubtitle": "Subtitle not defined",
            "activityImage": _default_activity_image,
            "facts": [],
            "markdown": "true"
        }]
    }

    def __init__(self, **kwargs):
        if kwargs:
            if 'summary' in kwargs:
                self.structure['summary'] = kwargs['summary']
                self.structure['sections'][0]['activityTitle'] = \
                    f"![TestImage]({self._default_activity_title_image}){kwargs['summary']}"
            if 'colour' in kwargs:
                self.structure['themeColor'] = kwargs['colour']
            if 'color' in kwargs:
                self.structure['themeColor'] = kwargs['color']
            if 'subtitle' in kwargs:
                self.structure['sections'][0]['activitySubtitle'] = kwargs['subtitle']
            if 'text' in kwargs:
                self.structure['sections'][0]['text'] = kwargs['text']

    def add_fact(self, name: str, value: str):
        self.structure['sections'][0]['facts'].append({"name": name, "value": value})

    def del_fact(self, name: str):
        _found_id = 0
        for fact in self.structure['sections'][0]['facts']:
            if fact.get('name') == name:
                return self.structure['sections'][0]['facts'].pop(_found_id)
            _found_id += 1
        return False

    def get_card(self):
        return self.structure
