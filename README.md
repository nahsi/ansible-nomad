# Nomad

Install, configure and maintain [Nomad](https://www.nomadproject.io) - A workload orchestrator from HashiCorp.

## Role Variables

See [defaults/](defaults/) for details and examples.

#### `nomad_version`

- version to use

#### `nomad_dirs`

- a map of directories to create

#### `nomad_config`

- main [configuration](https://www.nomadproject.io/docs/configuration) file

#### `Nomad_configs`

- map of configuration files to create in `config.d` directory. Restart on
  changes

#### `nomad_user`

- owner of Nomad process and files

#### `nomad_group`

- group of `nomad_user`

#### `nomad_download_url`

- url to get nomad archive from

#### `nomad_service`

- openrc service file

#### `nomad_unitfile`

- systemd unit file

#### `skip_handlers`

- skip nomad restart/reload - useful when building images with Packer

## Tags

- `config` - update nomad unit/service file and sync configuration files

## Author

- **Anatoly Laskaris** - [nahsi](https://github.com/nahsi)
