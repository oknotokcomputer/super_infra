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
}


deps = {
  "build": {
    "url": "{chromium_git}/chromium/tools/build.git@f8363fc330fd1d8ce824539766503b7dbaf5a34d",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@90cf7feed9f3918abb484014d06aff344618cff6",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@4811b6ab06e6a52d24733716c424434ce0b4cedc",
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
    "url": "{chrome_internal_git}/infra/puppet.git@92a469e9b98b56b2ec1a3bb6729dd68b5f74514f",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@e962f2de4c1f1772d97b4915f44be5b43cbe9da1",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@82a5fa6d9cc4719cb4a5e9f2d948411790152f42",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@e583ee2570e655ae59ab59d3e0a8260a2129d962",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@ce66681a6aefb11eec2957dd4fb9c3947d180f0c",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@13950a8f418cd91388a1cc7761e87a0ade4e9bb0",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@f1fcc0435366454bf4d219ff0c8d17987e831262",
    "condition": "checkout_internal",
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