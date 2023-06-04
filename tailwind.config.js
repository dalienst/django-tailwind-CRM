/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'clients/templates/clients/*.html',
    'core/templates/core/*.html',
    'dashboard/templates/dashboard/*.html',
    'leads/templates/lead/*.html',
    'userprofile/templates/userprofile/*.html',
    'team/templates/team/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

