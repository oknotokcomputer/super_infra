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
    "url": "{chromium_git}/chromium/tools/build.git@dac5b1837e8f41b9e1085df2de37d9aab9f4eac9",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@6361a20b093bbd56984be4090cde9fc44bbcdd7b",
  },

  "recipes-py": {
    "url": "{chromium_git}/infra/luci/recipes-py.git@f4da958651245c502ddc163813f920c91adedd33",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@af05b5638133c5c11f4fc0414dac52d0d923859a",
    "condition": "checkout_internal",
  },

  "build_internal": {
    "url": "{chrome_internal_git}/chrome/tools/build.git@5975d3124739d2d96127b96dd4f991c36bcac0a5",
    "condition": "checkout_internal",
  },

  "puppet": {
    "url": "{chrome_internal_git}/infra/puppet.git@5b96f106e61f3e32c86d2ebe499b1dc42897d474",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@6851c8b77095ae886d33fce3bcfb43bc92366dda",
    "condition": "checkout_internal",
  },

  "data/cloud-run": {
    "url": "{chrome_internal_git}/infradata/cloud-run.git@6ec89ffac129daeb3f73ff4e63b34c91f89bde59",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@fad3b28aed2f88076144eb7513147b541b67f663",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@493d46b0d5145842eb9daf7bfea97b1531f6a0c0",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@3c61a54854d1fecb1e73fe2d51870b7bf8b151b4",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@d747c8251b6c0f8a2a1c5307ed9d840f17b70725",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@0a47744a34597a887f1b36e222aba71c72119ec1",
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
