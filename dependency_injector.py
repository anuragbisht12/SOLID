# This package handles object creation and dependency inversion to achieve dependency injection

from dependency_injector import providers, containers


class EmailClient(object):
    
    def __init__(self, config):
        self._config = config
        self.connect(self._config)
        
    def connect(self, config):
        # Implement function here
        pass


class EmailReader(object):
    
    def __init__(self, client):
        try:
            self._client = client
        except Exception as e:
            raise e
            
    def read(self):
        # Implement function here
        pass


class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')
    # other configs
    
class Clients(containers.DeclarativeContainer):
    email_client = providers.Singleton(EmailClient, Configs.config)
    # other clients
    
class Readers(containers.DeclarativeContainer):
    email_reader = providers.Factory(EmailReader, client=Clients.email_client)

if __name__ == "__main__":
    email_reader = Readers.email_reader()
    print email_reader.read()
