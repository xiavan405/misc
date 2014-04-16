class Singleton(object):
	instance = None

	def __init__(self):
		self._connection = 'foo'

	@staticmethod
	def get_instance():
		if Singleton.instance is None:
			Singleton.instance = Singleton()
		return Singleton.instance
