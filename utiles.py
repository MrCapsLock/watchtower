import ipaddress


class Validator:
    def __init__(self):
        pass

    def validate_input(self, args):
        name, ip, port, method, interval = args[1:]
        if (
            not self.validate_ip(ip)
            or not self.validate_port(port)
            or not self.validate_method(method)
            or not self.validate_interval(interval)
        ):
            return False
        return True

    def validate_ip(self, ip):
        try:
            if not ipaddress.ip_address(ip).is_private:
                return True
            return False
        except:
            return False

    def validate_port(self, port):
        try:
            port = int(port)
            if port > 0 and port <= 65535:
                return True
            return False
        except:
            return False

    def validate_method(self, method):
        if method == "ping" or method == "wget":
            return True
        else:
            return False

    def validate_interval(self, interval):
        try:
            interval = int(interval)
            if interval >= 60:
                return True
            return False
        except:
            return False


class Database:
    def __init__(self):
        pass

    def save(self):
        pass