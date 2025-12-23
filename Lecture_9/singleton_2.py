class Log:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            print("*Creating the log object for the first time*\n")
            cls.instance = super().__new__(cls)
        return cls.instance

    def log_info(self, message):
        print(f"INFO: {message}\n")

    def log_error(self, message):
        print(f"ERROR: {message}\n")

log1 = Log()
log1.log_info("Initializing log..")

log2 = Log()
log2.log_error("Log already initialized!")