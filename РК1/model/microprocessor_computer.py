class MicroprocessorComputer:
    """
    Микропроцессоры компютеров
    для реализации связи многие-ко-многим
    """

    def __init__(self, computer_id, microprocessor_id):
        self.microprocessor_id = microprocessor_id
        self.computer_id = computer_id