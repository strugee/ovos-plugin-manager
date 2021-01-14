from setuptools import setup

setup(
    name='ovos-plugin-manager',
    version='0.0.1',
    packages=['ovos_plugin_manager'],
    url='https://github.com/OpenVoiceOS/OVOS-plugin-manager',
    license='Apache-2.0',
    author='jarbasAi',
    install_requires=["ovos_utils>=0.0.5", "requests"],
    author_email='jarbasai@mailfence.com',
    description='OpenVoiceOS plugin manager'
)
