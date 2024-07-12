class Tile:
    def __init__(self, status_bar_height, nav_bar_height, header_height, footer_height, filepath=None, sha=None,
                 fullscreen=False) -> None:
        self.filepath = filepath
        self.status_bar_height = status_bar_height
        self.nav_bar_height = nav_bar_height
        self.header_height = header_height
        self.footer_height = footer_height
        self.fullscreen = fullscreen
        self.sha = sha

    def __iter__(self):
        properties = [
            {'key': 'filepath', 'value': self.filepath},
            {'key': 'status_bar_height', 'value': self.status_bar_height},
            {'key': 'nav_bar_height', 'value': self.nav_bar_height},
            {'key': 'header_height', 'value': self.header_height},
            {'key': 'footer_height', 'value': self.footer_height},
            {'key': 'fullscreen', 'value': self.fullscreen},
            {'key': 'sha', 'value': self.sha}
        ]

        for prop in properties:
            yield prop['key'], prop['value']
