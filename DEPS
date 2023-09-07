use_relative_paths = True

git_dependencies = "SYNC"

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
    "url": "{chromium_git}/chromium/tools/build.git@8838ee2750edbc1d8e756716008c2b3eb788db6f",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@965ec7dc219ed99a1f76ba5fc65535c2dd3748f8",
  },

  "recipes-py": {
    "url": "{chromium_git}/infra/luci/recipes-py.git@2cd5f04ab0884d75b3a27be1a8c739beccbbd8df",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@27bb8ab1f73c5328d4b21c3a623cc75954f339c9",
    "condition": "checkout_internal",
  },

  "build_internal": {
    "url": "{chrome_internal_git}/chrome/tools/build.git@0a2d1d592d83bb77b66aeeba55649ca5f5eba52f",
    "condition": "checkout_internal",
  },

  "puppet": {
    "url": "{chrome_internal_git}/infra/puppet.git@165495773090d0d0a3c12ae80afb08081441bd59",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@c5c2299ca5be0c8a669bee274ac02720c14fc3f1",
    "condition": "checkout_internal",
  },

  "data/cloud-run": {
    "url": "{chrome_internal_git}/infradata/cloud-run.git@ae968ba6221a811333803ab9fb7f60774134d873",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@4858282d0a282627359968f6f86eae888df399e1",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@b1a1828b478e8c41c65220a5e3adf46962a628fe",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@69f79e9f69b710acab1435764ff9939384a101c2",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@4705822bf0a93e48dd89ccd5088d7a8fabe03a5f",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@60bc88460a0b4d7c8bf1ee10ad301d66503dc88b",
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
