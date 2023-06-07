use_relative_paths = True

vars = {
  # This is used during the transition phase of moving infra repos to git
  # submodules. To add new deps here check with the Chrome Source Team.
  "infra_superproject_checkout": True,
  #
  # Set to True if internal repos should be checked out.
  "checkout_internal": False,

  'chromium_git': 'https://chromium.googlesource.com',
  'chrome_internal_git': 'https://chrome-internal.googlesource.com',

  # 'magic' text to tell depot_tools that git submodules should be accepted but
  # but parity with DEPS file is expected.
  'SUBMODULE_MIGRATION': 'True'
}


deps = {
  "build": {
    "url": "{chromium_git}/chromium/tools/build.git@a1fc4030046a5ee3f5662e2d5d7ca9deff9fda6e",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@e2a42f4f954451dc215f323cfd213a100870a3f0",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@b5715c1a89893ff727cf8b41dd7eeb01e14361fa",
    "condition": "checkout_internal",
  },

  "bcid": {
    "url": "{chrome_internal_git}/external/gob/team/bcid-software-team/provenance.git@" +
    "853c183f8c591f5d1eb17695125f0b5eb2d57abd",
    "condition": "checkout_internal",
  },

  "build_internal": {
    "url": "{chrome_internal_git}/chrome/tools/build.git@bb302e0208de89fc13645ba5e083c3e4b4840e33",
    "condition": "checkout_internal",
  },

  "puppet": {
    "url": "{chrome_internal_git}/infra/puppet.git@2c5af8c0a17e83fe4ae3537b288bcd3694f1416b",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@0857876603497d93a529d8d815f5b94f17668784",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@b8496501e21846dab9b05b6b1c0a85e75da38cc7",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@802998c0d89c54221291ba5de5a29edcda05787e",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@3e2ba8f1365ec28dd1c42d8f2e5b238e7b092dcb",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@2674225c4843f1873f477940605599f1cf663578",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@720851e0609299aab12d46944c1fe163b9da62ad",
    "condition": "checkout_internal",
  },

  "gcloud": {
    'packages': [
      {
        'package': 'infra/3pp/tools/gcloud/${{os=mac,linux}}-${{arch=amd64}}',
        'version': 'version:2@427.0.0.chromium.3',
      }
    ],
    'dep_type': 'cipd',
  },
}

hooks = [
  {
    "pattern": ".",
    "action": [
      "python3", "-u", "infra/bootstrap/remove_orphaned_pycs.py",
      "infra_internal"
    ],
  },
]

recursedeps = ["infra", "build", "build_internal", "infra_internal"]
