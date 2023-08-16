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
    "url": "{chromium_git}/chromium/tools/build.git@419a20d67319812620df94e6108b9fdf0d29beee",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@2dba9ddbb163e64057b51331c94498e61cf48b91",
  },

  "recipes-py": {
    "url": "{chromium_git}/infra/luci/recipes-py.git@a4d67972f7a24c741e7bf37743572857bdb5a827",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@52e5b78f200bc9435cc7d7c29b2f46b8e6ca18e1",
    "condition": "checkout_internal",
  },

  "build_internal": {
    "url": "{chrome_internal_git}/chrome/tools/build.git@db78226de2ed85ebd3640bb8491a02417d9da12e",
    "condition": "checkout_internal",
  },

  "puppet": {
    "url": "{chrome_internal_git}/infra/puppet.git@464cac881b89a06d5a37666c4149af3e8366ba53",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@a88511140a7d144c650fa433a53f238c504589bd",
    "condition": "checkout_internal",
  },

  "data/cloud-run": {
    "url": "{chrome_internal_git}/infradata/cloud-run.git@f0e3636b1c3fec186eb6f28f3e8cae8d5c0979a8",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@a24e8990cad8c8b6f8c220804e55942834884e6a",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@cee4bc7b11f2d3575373fd88a866e6a83f927b25",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@2a4a4bf68ddb29daa11410a1db84c9c46cc9ab05",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@e73c9a5e3a6bcfaed897874074d92c5266247663",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@870b979d98f901cbc980496887a0c1dc9d1af483",
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
