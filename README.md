
# Rancher Desktop Storage Performance Test

## Environment

- Apple M2 MacBook Air(24GB RAM)
- OS: Sonoma

## Optimal settings

Rancher Desktop is selected by default, but the storage write speed feels slow. So, I reviewed the virtualization engine and volume mount settings.

### Results

- QEMU/reverse-sshfs
- QEMU/9p(128kb)
- QEMU/9p(512kb)
- VZ/reverse-sshfs
- VZ/virtiofs
- Docker Desktop Default(vz/virtiofs)

## How to test

```bash
docker build -t storage-perf-test .
```

run
```bash
docker run --rm -v ./test_data:/app/test_data storage-perf-test 
```
