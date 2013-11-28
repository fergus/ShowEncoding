# coding=utf8
# Added updating on view activation to capture changes on application reload with open tabs (FS 20131129)
# Moved event handlers for on_load and on_post_save to no blocking async calls (FS 20131129)
import sublime, sublime_plugin

class EncodingPlugin(sublime_plugin.EventListener):
    def __init__(self):
        return
    def on_load_async(self, view):
        self.update_encoding(view)
    def on_post_save_async(self, view):
    	self.update_encoding(view)
    def on_activated_async(self, view):
        self.update_encoding(view)

    def update_encoding(self, view):
    	view.set_status('ShowEncodingPluginStatus', view.encoding() if view.encoding() != u'Undefined' else sublime.load_settings('Preferences.sublime-settings').get('default_encoding', 'Unknown Encoding'))
