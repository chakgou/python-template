from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True)

template = env.get_template('enc.yaml')

print(template.render({
	'vm': 'casronno',
	'users': ['gather', 'momo'],
	'technos': [{
		'label': 'jar',
		'pp': 'vsct_jar',
		'applications': [{
			'label': 'vsf',
			'plateform': 'prd1',
			'components': [{
				'label': 'jarser',
				'instances': 15
			}]
		}]
	}]
}))
