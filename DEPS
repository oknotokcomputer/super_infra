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
    "url": "{chromium_git}/chromium/tools/build.git@8db2b2f453bbbf7a14ca98e66e0198ba09bd67ca",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@a1d6927d665456ea42779ac1a22fb1e72060a65c",
  },

  "recipes-py": {
    "url": "{chromium_git}/infra/luci/recipes-py.git@8038bd0ecd65510e72102b5d07c4401e90604574",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@71c3b3785b214b335fa9439248a6892d3e7ac7bb",
    "condition": "checkout_internal",
  },

  "build_internal": {
    "url": "{chrome_internal_git}/chrome/tools/build.git@3b99389add4193a3a92c5afe78bc293cc4dee825",
    "condition": "checkout_internal",
  },

  "puppet": {
    "url": "{chrome_internal_git}/infra/puppet.git@76022a8fe62b4546940dfadb63c002f0e8d6d0e1",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@5da8c0c0d5563dcf0ae3fc653e997d7243779fb8",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@40f07b5908f9f77cb16e3bcb125e487bed7ef380",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@8e99914c9105d6df72d1abeee11b1e3cd89bd0c0",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@3637b0feff97cfa1e41de3eacf4ca0423117d8e7",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@4be544ee06a1546dec342b8b481652cc08e8631e",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@9d1743ebf6ca43ea9a1ae55c2cef3e3f308d564d",
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
