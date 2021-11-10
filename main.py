from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import (Color, RoundedRectangle)

Builder.load_file('pong.kv')


class MyLayout(Widget):
	pass


class RectWidget(Widget):
	def __init__(self, **kwargs):
		super(RectWidget, self).__init__(**kwargs)

		with self.canvas:
			Color(.85,.89,.96,1)
			RoundedRectangle(pos = (25,200), 
				size = (350,300), 
				radius = [(10, 10), (10, 10), (10, 10), (10, 10)])


class TextFirst(Widget):
	pass
#.69,.78,.90,1


class MyApp(App):
	def build(self):
		Window.clearcolor = (.69,.78,.90,1)
		Window.size = (400, 600)
		Window.add_widget(RectWidget())
		return MyLayout()


if __name__ == '__main__':
	MyApp().run()