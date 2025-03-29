import { cva } from '../../../../styled-system/css'

export const button = cva({
	base: {
		fontSize: 'big',
		padding: '10px 30px',
		background: 'blue',
		color: 'primary',
		borderRadius: '10px',
		cursor: 'pointer',
		transitionDuration: '0.2s',

		_hover: {
			color: 'bkg',
			outline: '2px solid {colors.bkg}',
			background: 'primary',
			transitionDuration: '0.2s'
		}
	}
})

export const secondaryButton = cva({
	base: {
		fontSize: 'common',
		padding: '10px 35px',
		background: 'gray',
		color: 'bkg',
		borderRadius: '1000px',
		cursor: 'pointer',
		transitionDuration: '0.2s',
		_hover: {
			color: 'primary',
			background: 'blue'
		}
	}
})
