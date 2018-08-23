# Dependencies

- python3
- nginx
- sopel


## Install

```
cd ~/Eingangsschalter
sudo ./install.sh
```

### Afterwards
- configurate nginx
- configurate sopel
  - edit ~/.sopel/default.cfg
  - restart ircbot with `sudo systemctl restart ircbot` or run `sudo ./install.sh` again

## Update
```
cd ~/Eingangsschalter
git pull
sudo ./install.sh
```
