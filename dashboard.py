from django.utils.translation import ugettext_lazy as _

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):

        # append an app list module for "Applications"
        self.children.append(modules.ModelList(
            _("Site Data"),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        # self.children.append(modules.ModelList(
        #     _("Security"),
        #     column=2,
        #     collapsible=False,
        #     models=('django.contrib.*',),
        # ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=2,
        ))
