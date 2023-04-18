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
    "url": "{chromium_git}/chromium/tools/build.git@ea97dbbebb33263111c5d238f654664352f4cad1",
  },

  "testing_support": {
    "url": "{chromium_git}/infra/testing/testing_support.git@3f5ce5775cceffe4fdc078205eefe2bc12f206d4",
  },

  "infra": {
    "url": "{chromium_git}/infra/infra.git@9a40f586fb3f547af4f6a6e0d5d6147a272e097c",
  },

  "infra_internal": {
    "url": "{chrome_internal_git}/infra/infra_internal.git@a02e26ed53a1db5089c2208157b64712199797bc",
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
    "url": "{chrome_internal_git}/infra/puppet.git@19daad0a5d0432304c3967d9e923235939c767b0",
    "condition": "checkout_internal",
  },

  "systems": {
    "url": "{chrome_internal_git}/chrome-golo/chrome-golo.git@3b30d559947a86523b3c9f100f9e164ecc9f7d83",
    "condition": "checkout_internal",
  },

  # Not runtime dependencies, just included for ease of development.
  "data/config": {
    "url": "{chrome_internal_git}/infradata/config.git@9cfee7e274716b0491d4178da8d2f3821e25c0a1",
    "condition": "checkout_internal",
  },

  "data/gae": {
    "url": "{chrome_internal_git}/infradata/gae.git@f8e0814d4d87e5087b991d123043b17b3dadef27",
    "condition": "checkout_internal",
  },

  "data/k8s": {
    "url": "{chrome_internal_git}/infradata/k8s.git@dcf73a5da7403ee4bdb11484a1ee8ae183914c33",
    "condition": "checkout_internal",
  },

  "data/rbe": {
    "url": "{chrome_internal_git}/infradata/rbe.git@3af09e99a466a93a39563e2e71905a90fcfbb4ff",
    "condition": "checkout_internal",
  },

  "release_scripts": {
    "url": "{chrome_internal_git}/chrome/tools/release/scripts.git@d84036f7b44703c49ec484fa9881811d82efe4e8",
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