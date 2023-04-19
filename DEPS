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
    "url": "{chromium_git}/chromium/tools/build.git@d0b037baf89fdca44233603a8dc63f25ba2abfc6",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@ee3065beb936ba09dfa422795234cd24a851e555",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@2cae3a77ed975f1902b14ec6f3a9535b92a4da77",
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
    "url": "{chrome_internal_git}/infra/puppet.git@c1bd5c0ff9eef5d89b6040af2fd99e53658f5393",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@97e0b6997ad545a1ab9b6a1754609766ba89747c",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@8ec4542d5d51467dcd1c02ac120df16e38c67234",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@fd19117477e00e838d9e8c6614c3fb04489ac959",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@2de9ef1be605793225803764f73776f16dbbf043",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@00421ea3d556c9c8c99f152dc6376221fc0eddd2",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@6d4ce4250cc476702eb75d0ee7c75e2ad8f78424",
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