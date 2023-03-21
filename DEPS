vars = {
  # This is used during the transition phase of moving infra repos to git
  # submodules. To add new deps here check with the Chrome Source Team.
  "infra_superproject_checkout": True,
  #
  # Set to True if internal repos should be checked out.
  "checkout_internal": False,

  'chromium_git': 'https://chromium.googlesource.com',
  'chrome_internal_git': 'https://chrome-internal.googlesource.com',
}


deps = {
  "infra_superproject/build": {
    "url": "{chromium_git}/chromium/tools/build.git@c10634b020f05d5099f781a2c56a56191b2948f2",
  },

  "infra_superproject/testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra_superproject/infra": {
    "url": "{chromium_git}/infra/infra.git@3ea70b2f0a4544d829a1d23f5e3e579fbfefa9d7",
  },

  "infra_superproject/infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@e44fd1ba0fc613cf28da23b277246042871c54a3",
    "condition": "checkout_internal",
  },

  "infra_superproject/bcid": {
    "url": "{chrome_internal_git}/external/gob/team/bcid-software-team/provenance.git@" +
    "853c183f8c591f5d1eb17695125f0b5eb2d57abd",
    "condition": "checkout_internal",
  },

  "infra_superproject/build_internal": {
    "url": "{chrome_internal_git}/chrome/tools/build.git@9e199e141b4b2ce2388cfaa921bd7148b510a02b",
    "condition": "checkout_internal",
  },

  "infra_superproject/puppet": {
    "url": "{chrome_internal_git}/infra/puppet.git@e8e0d0cfc7235897035fffbf884cd9fb3c1c882f",
    "condition": "checkout_internal",
  },

  "infra_superproject/systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@c238652fd9211f90f72087f2c46841c5a916faf9",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "infra_superproject/data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@f2d808f2aa21035f2eac41a8a155e2c3c21b1ae4",
    "condition": "checkout_internal",
  },

  "infra_superproject/data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@223b8232cf20dbc5422d74256cdd9e626c19380c",
    "condition": "checkout_internal",
  },

  "infra_superproject/data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@3c1e0af7340df45093ad5350a35bb7c30c09c0b6",
    "condition": "checkout_internal",
  },

  "infra_superproject/data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@b6c1b63aee500eeb415865343a7dfd0aa6dee7a3",
    "condition": "checkout_internal",
  },

  "infra_superproject/release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@55753574da98d14d7992145a40270c68f1a37c60",
    "condition": "checkout_internal",
  },
}

hooks = [
  {
    "pattern": ".",
    "action": [
      "python3", "-u", "infra_superproject/infra/bootstrap/remove_orphaned_pycs.py",
      "infra_internal"
    ],
  },
]

recursedeps = ["infra_superproject/infra", "infra_superproject/build", "infra_superproject/build_internal"]