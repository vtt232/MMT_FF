import subprocess
import winreg as wr

# 1: String
# 3: Binary
# 4: Dword
# 11: Qword
# 7: Multiple strings
# 2: Expandable strings


class RegistryManager:
    def import_registry_file(self, reg_file):
        subprocess.call(['reg', 'import', reg_file])

    def conenct_registry_key(self, key):
        areg = wr.ConnectRegistry(None, key)
        return areg

    def get_data_type_number(self, data_type_string):
        data_type_string = data_type_string.rstrip()
        if data_type_string == "String":
            return 1
        if data_type_string == "Binary":
            return 3
        if data_type_string == "DWORD":
            return 4
        if data_type_string == "QWORD":
            return 11
        if data_type_string == "Multi-String":
            return 7
        if data_type_string == "Expandable String":
            return 2

    def get_hive(self, hive_string):
        if hive_string == "HKEY_CLASSES_ROOT":
            return wr.HKEY_CLASSES_ROOT
        elif hive_string == "HKEY_CURRENT_USER":
            return wr.HKEY_CURRENT_USER
        elif hive_string == "HKEY_CURRENT_CONFIG":
            return wr.HKEY_CURRENT_CONFIG
        elif hive_string == "HKEY_DYN_DATA":
            return wr.HKEY_DYN_DATA
        elif hive_string == "HKEY_LOCAL_MACHINE":
            return wr.HKEY_LOCAL_MACHINE
        elif hive_string == "HKEY_PERFORMANCE_DATA":
            return wr.HKEY_PERFORMANCE_DATA
        elif hive_string == "HKEY_USERS":
            return wr.HKEY_USERS

    def get_all_subkeys(self, hive, key_name):
        try:
            akey = wr.OpenKey(hive, key_name)
            index = 0
            subkeys = dict()
            while True:
                try:
                    name, value, _ = wr.EnumValue(akey, index)
                    subkeys[name] = value
                    index += 1
                except:
                    break
            
            return subkeys
        except Exception as e:
            print(str(e))

    def convert_value(self, value, data_type):
        if data_type == 3:
            return bytearray(value, "utf-8")
        if data_type == 7:
            return value.split(',')
        if data_type == 4 or data_type == 11:
            return int(value)
        return value

    def get_subkey_value(self, hive, key_name, sub_key):
        subkeys = self.get_all_subkeys(hive, key_name)
        return subkeys[sub_key]

    def set_subkey_value(self, hive, key_name, subkey, value, data_type=None):
        akey = wr.OpenKey(hive, key_name, 0, wr.KEY_ALL_ACCESS)
        value = self.convert_value(value, data_type)
        wr.SetValueEx(akey, subkey, 0, data_type, value)


    def delete_subkey(self, hive, key_name, sub_key):
        akey = wr.OpenKey(hive, key_name, 0, wr.KEY_ALL_ACCESS)
        wr.DeleteValue(akey, sub_key)

    def delete_all_subkeys(self, hive, key_name):
        subkeys = self.get_all_subkeys(hive, key_name)
        for subkey in subkeys:
            self.delete_subkey(hive, key_name, subkey)

    def delete_key(self, hive, key_name):
        self.delete_all_subkeys(hive, key_name)
        akey = wr.OpenKey(hive, key_name, 0, wr.KEY_ALL_ACCESS)
        wr.DeleteKey(akey, "")

    def create_key(self, hive, key_name):
        wr.CreateKey(hive, key_name)