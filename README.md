
```markdown
# MAC Address Changer

A Python script to change the MAC address of a specified network interface. This tool is helpful for testing, security, and privacy purposes.

## Features

- Changes the MAC address of a specified network interface (e.g., `eth0`).
- Validates user input and provides helpful error messages.
- Retrieves the current MAC address and confirms if it successfully changed.
- **Security**: Uses safe methods to avoid command injection vulnerabilities.

## Requirements

- **Python 3**
- **Admin Privileges**: This script requires `sudo` to execute commands on the network interface.

## Usage

1. Clone this repository or download the script.
2. Run the script with administrative privileges to change the MAC address.

```bash
sudo python3 spoofmac.py -i <interface> -m <new_mac_address>
```

Example:
```bash
sudo python3 spoofmac.py -i eth0 -m 00:22:44:66:88:10
```

## Code Breakdown

### Imports

- **`subprocess`**: Executes system commands to manage network settings.
- **`optparse`**: Parses command-line arguments.
- **`re`**: Uses regular expressions to locate MAC addresses.

### Functions

- **`get_arguments()`**: 
  - Sets up and validates command-line arguments.
  - Defines options:
    - `-i` or `--interface`: Network interface to modify.
    - `-m` or `--mac`: New MAC address for the interface.
  - Returns errors if required arguments are missing.

- **`mac_changer(interface, new_mac)`**:
  - Disables the network interface to avoid connectivity issues.
  - Sets the new MAC address.
  - Re-enables the interface to restore connectivity.
  - Prints a success message after completion.

- **`get_current_mac(interface)`**:
  - Retrieves and displays the current MAC address of the specified interface.
  - Uses a regular expression to ensure only MAC address format (e.g., `00:22:44:66:88:10`) is captured.

### Security Considerations

- **Command Injection Prevention**: By using a list format in `subprocess.call()` and `subprocess.check_output()`, this script avoids security risks associated with command injection. For instance, if the user inputs `eth0; ls`, the script won’t execute unintended commands.
- **Regex Validation**: Extracts only the MAC address format, filtering out invalid inputs.

## Example Output

```plaintext
Current MAC: 00:22:44:66:88:10
Changing MAC address of eth0 to 00:aa:bb:cc:dd:ee
MAC address successfully changed to 00:aa:bb:cc:dd:ee
```


