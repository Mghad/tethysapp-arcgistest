from tethys_sdk.base import TethysAppBase, url_map_maker


class Arcgistest(TethysAppBase):
    """
    Tethys app class for Arcgistest.
    """

    name = 'Arcgistest'
    index = 'arcgistest:home'
    icon = 'arcgistest/images/icon.gif'
    package = 'arcgistest'
    root_url = 'arcgistest'
    color = '#f39c12'
    description = 'My app is pretty cheesy'
    tags = 'cheese, ArcGIS'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='arcgistest',
                controller='arcgistest.controllers.home'
            ),
        )

        return url_maps
