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
    "url": "{chromium_git}/chromium/tools/build.git@eac6410e59fa32517a3087b7847b078699036e0a",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@e9fe06fd3df258bff2efaeeb36e537ab01e0b50c",
  },

  "recipes-py": {
    "url": "{chromium_git}/infra/luci/recipes-py.git@a4d67972f7a24c741e7bf37743572857bdb5a827",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@3b5d9182ef26a846b9028635e87ca7a9ca9f37a0",
    "condition": "checkout_internal",
  },

  "build_internal": {
    "url": "{chrome_internal_git}/chrome/tools/build.git@d899a297d795e0c8a1ddf897150c314aa68895d9",
    "condition": "checkout_internal",
  },

  "puppet": {
    "url": "{chrome_internal_git}/infra/puppet.git@f415c1d9720637eb9247e40d396d780e3f3ea2a3",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@50e7588798ffdaad53c830bba864ccf7a2a16a88",
    "condition": "checkout_internal",
  },

  "data/cloud-run": {
    "url": "{chrome_internal_git}/infradata/cloud-run.git@35ec41f506986094bc821dfbd6d9af2d3eb82e7f",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@0ec9d756b1f56c9f4aa226e8af5708416bb033b4",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@2e0287429f56aa720ecf86885aeb2a4775d69c71",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@23fbf75c2d80bdd1a437f8f6a2bd073d895cfe23",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@1c2f6f2ac5326628c3db1593e4ad7615ca28ca3b",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@f87682dc9ada42d8d77bd200473cdceb470dece4",
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
