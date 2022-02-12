import testinfra.utils.ansible_runner
import pytest
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.mark.parametrize("dirs", [
    "/opt/nomad/",
    "/opt/nomad/config.d/",
    "/var/lib/nomad/"
])
def test_directories_creation(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/opt/nomad/nomad.json",
    "/opt/nomad/config.d/log_level.json"
])
def test_file_creation(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file

@pytest.mark.parametrize("files", [
    "/opt/nomad/config.d/dummy.json",
])
def test_file_sync(host, files):
    f = host.file(files)
    assert not f.exists


@pytest.mark.parametrize("service", [
    "nomad"
])
def test_service_is_running(host, service):
    service = host.service(service)

    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize("port", [
    "4646"
])
def test_socket(host, port):
    s = host.socket("tcp://127.0.0.1:{}".format(port))
    assert s.is_listening
