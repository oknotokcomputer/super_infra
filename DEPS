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
    "url": "{chromium_git}/chromium/tools/build.git@ec85d440fe1500bdafa70b41daeac20ec73fbd27",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@6b6e5c549e01cf0c23bdfa50016c2d3a7b24e648",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@13b414f631f1e923d0510855093a619840229ba3",
    "condition": "checkout_internal",
  },

  "bcid": {
    "url": "{chrome_internal_git}/external/gob/team/bcid-software-team/provenance.git@" +
    "853c183f8c591f5d1eb17695125f0b5eb2d57abd",
    "condition": "checkout_internal",
  },

  "build_internal": {
    "url": "{chrome_internal_git}/chrome/tools/build.git@f94e21f022a0f65490946c5d02306fa2e6159566",
    "condition": "checkout_internal",
  },

  "puppet": {
    "url": "{chrome_internal_git}/infra/puppet.git@7790b5774889d9ccf91724bfb136e903ee53a687",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@1014d5764642945091501aac2a8f010b380e0625",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@d02d48cb4c8e258fb2c023d40083d5c6fd3a00a7",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@96089fa4fc9db1bdb77337e3555da5b5d4b770ff",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@bde7af57cd65cef8995e4d3586cb98fb71cf82cb",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@340b8139e933d81650510d8b550ac14702c16f20",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@48ea61173bd41e3559db04299e47c083a38e5410",
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

recursedeps = ["infra", "build", "build_internal"]