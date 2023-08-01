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
    "url": "{chromium_git}/chromium/tools/build.git@ce4926f0185ef4af00f07e741a008482ced4ac69",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@8110821287c9bcf418c9c9e03aea1e4078a12270",
  },

  "recipes-py": {
    "url": "{chromium_git}/infra/luci/recipes-py.git@e44c0c20fe61766b684e26dcd37eec2d161cf9f4",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@ecdf301becbe34b8fe5fdecfafba2d8da59aa6f0",
    "condition": "checkout_internal",
  },

  "build_internal": {
    "url": "{chrome_internal_git}/chrome/tools/build.git@2a5f3ddb5d2b95ef131a4ab3265c3bb036ac0f1b",
    "condition": "checkout_internal",
  },

  "puppet": {
    "url": "{chrome_internal_git}/infra/puppet.git@aa7241557e7d4d21582197e81aa0c81226dd3732",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@176f31e5eeae23423c697eaa8c77c4fc193bde08",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@0de55970d7b75ebdc5178d0f3716b13ab110692a",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@af03ce2f6790863c388398cd3576f2b4443b6334",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@eb513dad9288ceb06c16bde61b220a05ccacf0c0",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@6d939d8bbc11882d35f618ec96f0c25beacb4464",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@6ab017f4c3c88107f03431797bb910aad5ffb935",
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
