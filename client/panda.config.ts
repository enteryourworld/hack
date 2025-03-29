import { defineConfig } from '@pandacss/dev'

export default defineConfig({
	// Whether to use css reset
	preflight: true,

	// Where to look for your css declarations
	include: ['./src/**/*.{js,jsx,ts,tsx}', './pages/**/*.{js,jsx,ts,tsx}'],

	// Files to exclude
	exclude: [],

	// Useful for theme customization
	theme: {
		extend: {
			tokens: {
				colors: {
					primary: { value: '#FFFFFF' },
					secondary: { value: '#000000' },
					bkg: { value: '#35477D' },
					bkg_second: { value: '#ED3B4E' },
					bkg_light: { value: '#8BA2E9' }
				},
				fontSizes: {
					common: { value: '18px' },
					large: { value: '58px' }
				},
				spacing: {
					between_section: { value: '100px' }
				},
				shadows: {
					around: {
						value: {
							offsetX: 4,
							offsetY: 4,
							blur: 16,
							spread: 2,
							color: 'rgba(0, 0, 0, 0.25)'
						}
					}
				}
			}
		}
	},
	globalCss: {
		body: {
			bg: 'bkg'
		}
	},

	// The output directory for your css system
	outdir: 'styled-system'
})
