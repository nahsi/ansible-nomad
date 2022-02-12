# Nomad

Install, configure and maintain [nomad](https://www.nomadproject.io) - a
workload orchestrator from HashiCorp.

## Role Philosophy

Please see
[ansible-consul](https://github.com/nahsi/ansible-consul#role-philosophy).

## Role Variables

See [defaults/](https://github.com/nahsi/ansible-nomad/blob/master/defaults/)
for details and examples.

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
- example: please see
  [defaults/example.yml](https://github.com/nahsi/ansible-nomad/blob/master/defaults/example.yml)

#### `nomad_configs`

- map of configuration files to create in `config.d` directory

#### `nomad_user`

- owner of nomad process and files. Set to `nomad` on server hosts. On client
  hosts `root` is required.
- default: `root`

#### `nomad_grop`

- group of `nomad_user`. Set to `nomad` on server hosts.
- default: `root`

#### `nomad_download_url`

- url to get nomad archive from
- default: `https://releases.hashicorp.com`

#### `nomad_service`

- openrc service file
- default: see
  [defaults/main.yml](https://github.com/nahsi/ansible-nomad/blob/master/defaults/main.yml)

#### `nomad_unitfile`

- systemd unit file
- default: see
  [defaults/main.yml](https://github.com/nahsi/ansible-nomad/blob/master/defaults/main.yml)

#### `skip_handlers`

- skipt consul restart/reload - useful when building images with packer
- default: `false`

## Tags

- `config` - update nomad unit/service file and sync configuration files

## Author

- **Anatoly Laskaris** - [nahsi](https://github.com/nahsi)
