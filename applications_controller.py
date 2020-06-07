import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper



def all_application_questions():
    return sorted(yaml.load(open("application.yml", "r").read(), Loader=Loader), 
        key=lambda question: question['position'])
