import { Plus } from 'lucide-react'
import React from 'react'

import { button } from '@/shared/styles/reciepts/button'
import { input } from '@/shared/styles/reciepts/input'

import { css } from '../../../../styled-system/css'
import { hstack, vstack } from '../../../../styled-system/patterns'

interface IProps {
	className?: string
}

const Filters = ({ className }: IProps) => {
	return (
		<div className={hstack({ marginTop: '20px' })}>
			<div className=''>
				<input type='text' placeholder='От' />
				<input type='text' placeholder='до' />
			</div>
		</div>
	)
}

export default Filters
