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
    "url": "{chromium_git}/chromium/tools/build.git@7895834ecc596f2c0c8bba4503a23055ef12ae4d",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@726f53dc130f45eeb8492da3c7e1a2d50c05a727",
  },

  "recipes-py": {
    "url": "{chromium_git}/infra/luci/recipes-py.git@2cd5f04ab0884d75b3a27be1a8c739beccbbd8df",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@7b4b5b93978069fd920a03a6a7a4cb3e24bb90c1",
    "condition": "checkout_internal",
  },

  "build_internal": {
    "url": "{chrome_internal_git}/chrome/tools/build.git@a24832ca6f6b4be1d683cf96fd41dda4ab7c8d1e",
    "condition": "checkout_internal",
  },

  "puppet": {
    "url": "{chrome_internal_git}/infra/puppet.git@e5a3f421195f321edd1cd1dc5867a386e9bacc60",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@e00b634ba585bc60331332066fa286ebe4292891",
    "condition": "checkout_internal",
  },

  "data/cloud-run": {
    "url": "{chrome_internal_git}/infradata/cloud-run.git@9d00f02b160fd418307ab5a192f644d06a5f6256",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@2946dc8d2925c04663c0843d81deee3851357d97",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@d4140f2a55ca64e216349ae42793862ff9761ddb",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@19105b9f2b7e437aa6df2a4ab30a0cc4d7696089",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@f39df28095c3c217fbd51ac352134036b00bc20d",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@c30c55878fbb0ac86913c2fd05b8d1af27e4d88c",
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
