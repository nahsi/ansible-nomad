# nomad
Install, configure and maintain [nomad](https://www.nomadproject.io) - a workload orchestrator from HashiCorp.

## Role Philosophy
Instead of duplicating every single configuration option as an ansible variable configuration is stored in ansible inventory in yaml format:
```yml
nomad_config: 
  data_dir: "/var/lib/nomad/"

  enable_syslog: true
  # "trace", "debug", "info", "warn", "err"
  log_level: "info"
  syslog_facility: "LOCAL5"

  rejoin_after_leave: true

  bind_addr: !unsafe '{{ GetInterfaceIP "eth0" }}'

  telemetry:
    disable_compat_1.9: true
    disable_hostname: true
    prometheus_retention_time: "30s"

  server:
    enabled = true
```

And then copied to host using `no_nice_json` filter:
```yml
- name: copy nomad config
  copy:
    content: "{{ nomad_config | to_nice_json }}"
    dest: "/opt/nomad/nomad.json"
```

When variable is a map (`nomad_configs` for example) every key of a map will be copied as file with value as a content into directory (`/opt/nomad/config.d` for example). Files that are not present in the map will be deleted, thus allowing to maintain a state with ansible inventory.

## Role Variables
See [defaults/](defaults/) for details and examples.

#### `nomad_version`
- version to use
#### `nomad_dirs`
- a map of directories to create
- default:
```yml
nomad_dir: "/opt/nomad"
nomad_dirs:
  main:
    path: "{{ nomad_dir }}"
  configs:
    path: "{{ nomad_dir }}/config.d"
  certs:
    path: "{{ nomad_dir }}/certs"
    mode: "u=rwX,g=rX,o="
  logs:
    path: "/var/log/nomad"
  data:
    path: "/var/lib/nomad"
    mode: "u=rwX,g=rX,o="
```
#### `nomad_config`
- main [configuration](https://www.nomadproject.io/docs/configuration) file
#### `nomad_configs`
- map of configuration files to create in `config.d` directory
#### `nomad_user`
- owner of nomad process and files
- default: `root`
#### `nomad_grop`
- group of `nomad_user`
- default: `root`
#### `nomad_download_url`
- url to get nomad archive from
- default: `https://releases.hashicorp.com`
#### `nomad_service`
- openrc service file
- default: see [defaults/main.yml](defaults/main.yml)
#### `nomad_unitfile`
- systemd unit file
- default: see [defaults/main.yml](defaults/main.yml)
#### `skip_handlers`
- skipt consul restart/reload - useful when building images with packer

## Tags
* `config` - update nomad unit/service file and sync configuration files

## Author
* **Anatoly Laskaris** - [nahsi](https://github.com/nahsi)
