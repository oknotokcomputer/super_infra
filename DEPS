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
    "url": "{chromium_git}/chromium/tools/build.git@8b0f72c4a1d2da73309ab747599934149df7ec3a",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@420de34b79de377fb4613aef88d0cd9b6d9a040e",
  },

  "recipes-py": {
    "url": "{chromium_git}/infra/luci/recipes-py.git@c9aad4d94e4210dadc962bd0104b5a4444850fb1",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@7a7638409b469ba4646cb9ff124eccb8d978daaf",
    "condition": "checkout_internal",
  },

  "build_internal": {
    "url": "{chrome_internal_git}/chrome/tools/build.git@5a940af69aa38b5dfbef9be03721d69fbace1d43",
    "condition": "checkout_internal",
  },

  "puppet": {
    "url": "{chrome_internal_git}/infra/puppet.git@9c15fa175f8857ab25da83d786e386f313f340f0",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@aaae678d976b935e2a1aca2927160322efcd54e0",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@7b87744b5bfaa2e1d685ecf0d6789786d17ca08a",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@f31041581e8974bd436f926beb81bd6cc336d4ae",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@ba897efa8c4541e64458e88b592f613a232710a6",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@b6d0c9d7fe78043d8216529ab2ae3d1df688ce83",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@a160f18891f4bb0a8556fe3b9d6ee417c9dbd71f",
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
