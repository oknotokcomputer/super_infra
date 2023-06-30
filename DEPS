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
    "url": "{chromium_git}/chromium/tools/build.git@ad5cd53b730b2e60fe6ec5e97569c5c8444dbd93",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@6427432f19b30341ed05e8ccae6f3032f10fc98b",
  },

  "recipes-py": {
    "url": "{chromium_git}/infra/luci/recipes-py.git@84baae1fe070d4c73fe8d8acf936040db5b80979",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@d735d97d54aa52b44c54f7d1f059bcb03b08b0af",
    "condition": "checkout_internal",
  },

  "build_internal": {
    "url": "{chrome_internal_git}/chrome/tools/build.git@bb302e0208de89fc13645ba5e083c3e4b4840e33",
    "condition": "checkout_internal",
  },

  "puppet": {
    "url": "{chrome_internal_git}/infra/puppet.git@49bb3b3b8d2359e261f5e3d6be9e18ca8ec0f741",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@e21e08fc958ad8fbdf00f1836a5b14ae4bef6667",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@71cccd04b3477f2dad1caceefdd91be0f2a6ed05",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@a9bb4a0573db644bc8af1bd39a45483a1f7da4f0",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@7e1a11e0f9241602d68cce19cb86738464861762",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@cae5bbdb085e1b46e510a972dfa4247b2e608e62",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@8999d523f001faa6cca182cf66a4159ff55c59fe",
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
